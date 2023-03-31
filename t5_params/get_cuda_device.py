def get_cuda_command(cuda_device_nvidia):
    _cuda = {'cuda:5': 'cuda:3',
             'cuda:1': 'cuda:4',
             'cuda:2': 'cuda:5',
             'cuda:0': 'cuda:0',
             'cuda:3': 'cuda:1',
             'cuda:4': 'cuda:2'}
    _device = _cuda[cuda_device_nvidia][-1]
    return f'os.environ["CUDA_VISIBLE_DEVICES"]="{_device}"'