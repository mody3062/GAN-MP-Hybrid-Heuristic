
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
import numpy as np
import ipyparallel as ipp
        
def sample_Z(m, n):
    return Variable(torch.Tensor(np.random.rand(m, n)))


def xavier_init(size):
    in_dim = size[0]
    xavier_stddev = 1. / np.sqrt(in_dim / 2.)
    return np.random.normal(size=size, scale=xavier_stddev)



#@ipp.require(xavier_init)
class Generator(nn.Module):
    #@ipp.require(xavier_init)

    def __init__(self,  in_dim=10, hd_dim=50, out_dim=500):
        super(Generator, self).__init__()
        
        self.G_W1 = nn.Parameter(torch.from_numpy(xavier_init([in_dim, hd_dim])).float())
        self.G_b1 = nn.Parameter(torch.from_numpy(np.zeros(shape=[hd_dim])).float())
        #print('w1',self.G_W1)

        
        self.G_W12 = nn.Parameter(torch.from_numpy(xavier_init([hd_dim, hd_dim])).float())
        self.G_b12 = nn.Parameter(torch.from_numpy(np.zeros(shape=[hd_dim])).float())
        
        self.G_W13 = nn.Parameter(torch.from_numpy(xavier_init([hd_dim, hd_dim])).float())
        self.G_b13 = nn.Parameter(torch.from_numpy(np.zeros(shape=[hd_dim])).float())
        
        self.G_W2 = nn.Parameter(torch.from_numpy(xavier_init([hd_dim, out_dim])).float())
        self.G_b2 = nn.Parameter(torch.from_numpy(np.zeros(shape=[out_dim])).float())
        


    def forward(self, x=None):

        x = F.relu( x @ self.G_W1 + self.G_b1)
        x = F.relu( x @ self.G_W12 + self.G_b12)
        #x = F.relu( x @ self.G_W13 + self.G_b13)
        x = x @ self.G_W2 + self.G_b2


        return F.sigmoid(x*0.1)