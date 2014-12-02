fofix-rewrite
=============

Frets on Fire X, but rewritten from scratch.

This is probably going to be a very slow moving project.

Generally my goal for this project is: fofix-lite. Less features, less bloat, cleaner code, more speed.

Some general items for the future.
* Go through and take a second look at the general archetecture that has carried over from fofix.
* Bring in the math library.
* Bring the OpenGL binding back in. (faster than PyOpenGL, mostly compatible with PyOpenGL, only a partial binding)
* Start work rendering (Textures, shaders, etc).
* Font rendering, will be using freetype-py since sdl's sdl-ttf doesn't allow for "correct" letter spacing/kerning.
* Bring over various bits of code from the main fofix repository, such as MixStream on the audio side of stuff.
* Create/find a libsmf python binding for midi files.
* Design/build an easy to use and flexible system for creating all UI elements in the game. (Menu's, rockmeters, etc)
  * This is mainly for ease of theming.
* Probably more.
