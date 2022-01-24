def handle_errors(func):
    """Implements the error system by try-excepting `func` callback.

    :param func: any function that's first parameter is a Discord Context object
    :preconditi
    :precondition: `func.__name__` must be prefixed with '_com'


    :return: inner function containing try-catched version of `func`
    """

    async def inner(*args, **kwargs):
        context = args[1]
        try:
            await func(*args, **kwargs)
        except NotImplementedError:
            await context.send(f"🚧🚧 This command is still under development!! 🚧🚧")
        except Exception as e:
            print('error:', e)

    name = func.__name__
    func.__name__ = ''
    inner.__name__ = name
    return inner
