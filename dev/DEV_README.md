First version works!

Now, let's add more features!

## Section 1: refactoring

- move dp.update.outer_middleware to setup_dispatcher? or somewhere ... 
- move to plugin 'message_history'
  - config to enable/disable plugin
  - import dependencies only on ...
  - 
- use app somehow? 

## section 2: where to save
- to memory
- to disk
- ... to database (if enabled)

# Section 3: functionality (out of the box)
- get messages for user
- get messages for chat

- bot -> get message obj.
- donwload / load files on demand.

# Section 4: message streams
- a) main app messages collection (with data, i guess)
- b) archive messages collection (raw, as is, as a backup)
- c) message dumps loads - from pyrogram


