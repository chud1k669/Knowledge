def get_data_fig(*args, **kwargs):
    n = ['tp', 'color', 'closed', 'width']
    return (sum(args), *[kwargs[i] for i in n if i in kwargs])