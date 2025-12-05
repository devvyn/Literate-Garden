pico-8 cartridge // http://www.pico-8.com
version 43
__lua__
-- barkour: tilly's dream
-- bacon-powered parkour!

-- shared architecture:
-- uses same physics params
-- as pygame and web versions

-- === init ===
function _init()
  -- game state
  victory=false
  victory_timer=0
  frame=0  -- for notifications

  -- player (tilly!)
  p={
    x=20,y=460,     -- pos (start at bottom)
    dx=0,dy=0,      -- vel
    w=6,h=6,        -- size
    grounded=false,
    wall=nil,       -- "l"/"r"/nil
    can_wj=false,   -- can wall jump
    powered=false,
    ptimer=0,       -- power timer
    particles={},   -- wall slide fx
    start_x=20,     -- respawn point
    start_y=460
  }

  -- physics (scaled for pico-8)
  -- 128x128 screen needs gentler values
  cfg={
    grav=0.3,      -- gentler gravity
    jump=-6,       -- much lower jump
    spd=2,         -- slower movement
    accel=0.5,     -- acceleration
    friction=0.8,  -- deceleration
    max_fall=8,    -- lower terminal vel
    wslide=1.5,    -- wall slide
    wpush=4,       -- wall jump push
    wjump=-7,      -- wall jump str

    -- power-up multipliers
    pspd=1.5,
    pjump=1.3,
    pwjump=1.4
  }

  -- vertical tower (4 screens: 512px tall)
  -- screen 1: ground (tutorial)
  -- screen 2: buildings
  -- screen 3: rooftops
  -- screen 4: clouds (victory!)

  -- bacon spawns (strategically placed)
  bacon={
    -- screen 1: easy to find
    {x=60,y=450,c=false},
    -- screen 2: requires wall kick
    {x=10,y=340,c=false},
    -- screen 3: hidden side path
    {x=110,y=230,c=false},
    -- screen 3: another challenge
    {x=30,y=190,c=false},
    -- screen 4: reward for reaching top
    {x=64,y=60,c=false}
  }

  -- field specimens (aafc herbarium)
  specimens={
    -- rosa acicularis (prairie)
    {x=100,y=450,c=false,n="rosa acicularis",cn="wild rose"},
    -- carex praticola (wetland)
    {x=25,y=320,c=false,n="carex praticola",cn="meadow sedge"},
    -- picea glauca (boreal)
    {x=95,y=210,c=false,n="picea glauca",cn="white spruce"},
    -- cypripedium (rare orchid)
    {x=15,y=175,c=false,n="cypripedium acaule",cn="lady's slipper"},
    -- dryas octopetala (alpine)
    {x=64,y=45,c=false,n="dryas octopetala",cn="mountain avens"}
  }

  -- collection tracking
  specimens_found=0
  last_specimen=""

  -- platforms (ground → clouds)
  platforms={
    -- screen 1: ground (tutorial jumps)
    {x=0,y=480,w=128,h=16},   -- floor
    {x=15,y=450,w=35,h=4},    -- first jump
    {x=70,y=430,w=35,h=4},    -- second jump
    {x=20,y=400,w=30,h=4},    -- third jump
    {x=85,y=370,w=35,h=4},    -- up to screen 2

    -- screen 2: buildings (mixed challenges)
    {x=10,y=340,w=25,h=4},    -- wall kick practice
    {x=90,y=310,w=30,h=4},
    {x=30,y=280,w=40,h=4},    -- wider platform
    {x=80,y=250,w=35,h=4},    -- up to screen 3

    -- screen 3: rooftops (tricky)
    {x=15,y=220,w=25,h=4},    -- narrow platforms
    {x=90,y=200,w=25,h=4},
    {x=40,y=180,w=30,h=4},
    {x=85,y=150,w=30,h=4},
    {x=30,y=120,w=35,h=4},    -- up to screen 4

    -- screen 4: clouds (victory area)
    {x=50,y=90,w=30,h=4},     -- cloud platform
    {x=20,y=60,w=88,h=4},     -- big cloud (goal)
    {x=40,y=30,w=50,h=4}      -- victory platform
  }

  -- walls (for wall kicks)
  walls={
    -- screen 1: intro wall
    {x=5,y=380,w=4,h=80},

    -- screen 2: wall kick gauntlet
    {x=5,y=290,w=4,h=100},
    {x=119,y=240,w=4,h=120},

    -- screen 3: rooftop walls
    {x=10,y=150,w=4,h=100},
    {x=114,y=120,w=4,h=130},

    -- screen 4: final wall
    {x=60,y=40,w=4,h=80}
  }
end

-- === update (60fps) ===
function _update()
  -- input with acceleration
  local target_spd=cfg.spd
  if p.powered then
    target_spd*=cfg.pspd
  end

  if btn(⬅️) then
    p.dx=max(p.dx-cfg.accel,-target_spd)
  elseif btn(➡️) then
    p.dx=min(p.dx+cfg.accel,target_spd)
  else
    -- apply friction
    p.dx*=cfg.friction
    if abs(p.dx)<0.1 then p.dx=0 end
  end

  -- gravity
  if p.wall and p.dy>0 and not p.grounded then
    -- wall slide
    p.dy=min(p.dy+cfg.grav,cfg.wslide)

    -- add slide particle
    if #p.particles<3 then
      local px=p.wall=="l" and p.x or p.x+p.w
      add(p.particles,{
        x=px,
        y=p.y+p.h/2,
        life=20
      })
    end
  else
    p.dy+=cfg.grav
    if p.dy>cfg.max_fall then
      p.dy=cfg.max_fall
    end
  end

  -- update particles
  for part in all(p.particles) do
    part.life-=1
    part.y+=2
    if part.life<=0 then
      del(p.particles,part)
    end
  end

  -- jump
  if btnp(❎) or btnp(⬆️) then
    if p.grounded then
      -- ground jump
      local j=cfg.jump
      if p.powered then
        j*=cfg.pjump
      end
      p.dy=j
      p.grounded=false
    elseif p.can_wj then
      -- wall jump!
      local push=cfg.wpush
      p.dx=p.wall=="l" and push or -push

      local wj=cfg.wjump
      if p.powered then
        wj*=cfg.pwjump
      end
      p.dy=wj
      p.wall=nil
      p.can_wj=false
    end
  end

  -- move
  p.x+=p.dx
  p.y+=p.dy

  -- platform collision
  p.grounded=false
  for plat in all(platforms) do
    if collide_rect(p,plat) then
      if p.dy>0 then -- falling
        p.y=plat.y-p.h
        p.dy=0
        p.grounded=true
        p.wall=nil
      elseif p.dy<0 then -- jump into
        p.y=plat.y+plat.h
        p.dy=0
      end
    end
  end

  -- wall collision
  p.wall=nil
  for wall in all(walls) do
    if collide_rect(p,wall) then
      if p.dx>0 then
        p.wall="r"
      elseif p.dx<0 then
        p.wall="l"
      end
    end
  end
  p.can_wj=p.wall!=nil and not p.grounded

  -- bounds (prevent falling off)
  if p.x<0 then
    p.x=0
    p.dx=0
  end
  if p.x>128-p.w then
    p.x=128-p.w
    p.dx=0
  end

  -- bottom boundary (respawn)
  if p.y>500 then
    p.x=p.start_x
    p.y=p.start_y
    p.dx=0
    p.dy=0
    p.powered=false
  end

  -- victory condition (reach top)
  if not victory and p.y<50 then
    victory=true
    victory_timer=180  -- 3 sec
  end

  -- victory timer
  if victory then
    victory_timer-=1
    if victory_timer<=0 then
      -- restart
      _init()
    end
  end

  -- bacon collection
  for b in all(bacon) do
    if not b.c then
      if abs(p.x-b.x)<8 and abs(p.y-b.y)<8 then
        b.c=true
        p.powered=true
        p.ptimer=300 -- 5sec*60fps
        sfx(0) -- todo: bacon sfx
      end
    end
  end

  -- specimen collection
  for s in all(specimens) do
    if not s.c then
      if abs(p.x-s.x)<10 and abs(p.y-s.y)<10 then
        s.c=true
        specimens_found+=1
        last_specimen=s.cn
        frame=0  -- reset notification timer
        sfx(1) -- todo: specimen sfx
      end
    end
  end

  -- power timer
  if p.powered then
    p.ptimer-=1
    if p.ptimer<=0 then
      p.powered=false
    end
  end
end

-- === collision ===
function collide_rect(a,b)
  return a.x<b.x+b.w and
         a.x+a.w>b.x and
         a.y<b.y+b.h and
         a.y+a.h>b.y
end

-- === draw ===
function _draw()
  cls(12) -- sky blue

  -- camera follows player (vertical)
  local cam_y=max(0, min(p.y-64, 512-128))
  camera(0,cam_y)

  -- platforms
  for plat in all(platforms) do
    rectfill(plat.x,plat.y,
             plat.x+plat.w-1,
             plat.y+plat.h-1,
             4) -- brown
  end

  -- walls
  for wall in all(walls) do
    rectfill(wall.x,wall.y,
             wall.x+wall.w-1,
             wall.y+wall.h-1,
             5) -- gray

    -- texture lines
    for i=0,wall.h,5 do
      line(wall.x,wall.y+i,
           wall.x+wall.w,wall.y+i,
           6)
    end
  end

  -- bacon
  for b in all(bacon) do
    if not b.c then
      -- simple bacon rect
      -- (replace with sprite later)
      local by=b.y+sin(time()*2)*2
      rectfill(b.x,by,b.x+5,by+3,14)
      line(b.x,by+1,b.x+5,by+1,8)
    end
  end

  -- field specimens (aafc)
  for s in all(specimens) do
    if not s.c then
      -- green plant icon
      local sy=s.y+sin(time()*1.5)*1.5
      -- leaf shape
      circfill(s.x+2,sy,3,11)  -- green
      circfill(s.x+5,sy+2,3,11)
      line(s.x+3,sy+3,s.x+3,sy+6,3)  -- stem
      -- sparkle
      if flr(time()*4)%2==0 then
        pset(s.x+1,sy-2,7)
      end
    end
  end

  -- wall slide particles
  for part in all(p.particles) do
    local alpha=part.life/20
    circfill(part.x,part.y,1,7)
  end

  -- player glow (if powered)
  if p.powered then
    rectfill(p.x-2,p.y-2,
             p.x+p.w+2,p.y+p.h+2,
             10) -- yellow glow
  end

  -- player (tilly!)
  -- simple rect for now
  -- (replace with sprite)
  local col=p.powered and 10 or 4
  rectfill(p.x,p.y,
           p.x+p.w-1,p.y+p.h-1,
           col) -- beige or gold

  -- muzzle (black)
  rectfill(p.x+1,p.y+p.h-2,
           p.x+3,p.y+p.h-1,
           0)

  -- wall jump indicator
  if p.can_wj then
    local ix=p.wall=="l" and p.x-3 or p.x+p.w+1
    circfill(ix,p.y+p.h/2,2,11)
  end

  -- ui (fixed to camera)
  camera()  -- reset camera for ui

  if victory then
    -- victory screen!
    rectfill(0,0,128,128,0)
    local blink=flr(time()*4)%2==0
    if blink then
      print("☁️ you reached",28,50,7)
      print("the clouds! ☁️",26,58,7)
    end
    print("tilly's dream",28,70,12)
    print("came true!",32,78,10)

    -- specimen collection stats
    print("🌿 specimens: "..specimens_found.."/5",20,90,11)
    if specimens_found==5 then
      print("master naturalist!",22,98,10)
    end
  else
    -- normal ui
    if p.powered then
      -- power timer
      local t=flr(p.ptimer/60*10)/10
      print("ユかし⧗ bacon power",2,2,10)
      print(t.."s",2,8,10)
    end

    -- height indicator
    local height=flr((500-p.y)/500*100)
    print("⬆️ "..height.."%",90,2,7)

    -- specimen counter
    if specimens_found>0 then
      print("🌿 "..specimens_found.."/5",90,10,11)
    end

    -- specimen notification
    if last_specimen!="" and frame<180 then
      print("found: "..last_specimen,10,60,11)
      print("(aafc herbarium)",14,68,3)
    end

    -- controls reminder
    if p.y>400 and specimens_found==0 then
      print("climb to clouds!",20,118,7)
      print("find plants! 🌿",24,110,11)
    end
  end

  -- reset notification timer
  if last_specimen!="" then
    frame+=1
  end
end

