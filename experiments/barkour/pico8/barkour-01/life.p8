pico-8 cartridge // http://www.pico-8.com
version 42
__lua__
-- conway's game of life
-- colorful screensaver version

function _init()
  -- grid size (16x16 cells)
  w=16
  h=16
  cs=8  -- cell size

  -- create grid
  grid={}
  next_grid={}
  for x=0,w-1 do
    grid[x]={}
    next_grid[x]={}
    for y=0,h-1 do
      grid[x][y]=rnd()>0.7  -- random start
      next_grid[x][y]=false
    end
  end

  -- color palette cycling
  colors={8,9,10,11,12,14,15}
  col_idx=1
  frame=0
end

function _update()
  frame+=1

  -- update grid every 4 frames
  if frame%4==0 then
    -- calculate next generation
    for x=0,w-1 do
      for y=0,h-1 do
        local n=count_neighbors(x,y)

        if grid[x][y] then
          -- alive cell
          next_grid[x][y]=(n==2 or n==3)
        else
          -- dead cell
          next_grid[x][y]=(n==3)
        end
      end
    end

    -- swap grids
    local temp=grid
    grid=next_grid
    next_grid=temp
  end

  -- cycle colors
  if frame%30==0 then
    col_idx+=1
    if col_idx>#colors then col_idx=1 end
  end

  -- restart if all dead
  if frame%120==0 then
    local alive=false
    for x=0,w-1 do
      for y=0,h-1 do
        if grid[x][y] then alive=true end
      end
    end
    if not alive then
      _init()
    end
  end
end

function count_neighbors(x,y)
  local count=0
  for dx=-1,1 do
    for dy=-1,1 do
      if not (dx==0 and dy==0) then
        local nx=(x+dx)%w
        local ny=(y+dy)%h
        if grid[nx][ny] then
          count+=1
        end
      end
    end
  end
  return count
end

function _draw()
  cls(0)

  -- draw grid
  for x=0,w-1 do
    for y=0,h-1 do
      if grid[x][y] then
        local px=x*cs
        local py=y*cs

        -- pulsing effect
        local pulse=sin(time()*2+x*0.1+y*0.1)*2

        -- draw cell with glow
        rectfill(px,py,px+cs-1,py+cs-1,colors[col_idx])
        rect(px-1,py-1,px+cs,py+cs,7)
      end
    end
  end

  -- title
  print("conway's game of life",10,2,7)
  print("press z to randomize",10,120,6)

  -- stats
  local alive_count=0
  for x=0,w-1 do
    for y=0,h-1 do
      if grid[x][y] then alive_count+=1 end
    end
  end
  print("alive: "..alive_count,2,10,11)

  -- press z to randomize
  if btnp(❎) then
    _init()
  end
end
