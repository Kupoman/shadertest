import sdl2


class GraphicsContext:
    def __init__(self):
        self.window = None
        self.context = None

    def __enter__(self):
        sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        self.window = sdl2.SDL_CreateWindow(
            b'Shadertest',
            sdl2.SDL_WINDOWPOS_UNDEFINED,
            sdl2.SDL_WINDOWPOS_UNDEFINED,
            1,
            1,
            sdl2.SDL_WINDOW_OPENGL,
        )
        sdl2.video.SDL_GL_SetAttribute(sdl2.video.SDL_GL_CONTEXT_MAJOR_VERSION, 3)
        sdl2.video.SDL_GL_SetAttribute(sdl2.video.SDL_GL_CONTEXT_MINOR_VERSION, 3)
        sdl2.video.SDL_GL_SetAttribute(
            sdl2.video.SDL_GL_CONTEXT_PROFILE_MASK,
            sdl2.video.SDL_GL_CONTEXT_PROFILE_CORE,
        )
        self.context = sdl2.SDL_GL_CreateContext(self.window)

    def __exit__(self, *args):
        sdl2.SDL_GL_DeleteContext(self.context)
        sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()
