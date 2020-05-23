import torch.nn as nn

"""
The present python script contains the following classes:

* The Extractor class used to define the feature extractor (Resnet18 without the FC layer),***(Edoardo hai detto che lo facevi quindi te lo lascio)
* The Main_task class, used to perform the main task which a multi class classification
* The Pre_text class which is used to predict the relative rotation between the depth and the RGB modalities

"""

class Pre_text(nn.Module):
  """
  Pretext task
  
  """
  def __init__(self, num_classes = 4, featureMaps = 512, **kwargs):
    super(Pre_text, self).__init__():
      self.layer = nn.sequential(
            nn.Conv2d(featureMaps, 100, kernel_size = 1),
            nn.BatchNorm2d(100),
            nn.ReLU(inplace=True),
            nn.Conv2d(100, 100, kernel_size = 3),
            nn.BatchNorm2d(100),
            nn.ReLU(inplace=True),
            nn.Linear(100, 100),
            nn.Softmax(100),
            nn.Linear(100, num_classes),
      )
      
class  Main_task(nn.Module):
  """
  Main classifier
  """
  def__init__(self, num_classes = 51, featureMaps = 512, **kwargs):
    super(Main_task, self).__init__():
      self.layer = nn.Sequential(
            nn.AdaptiveAvgPool2d((7,7)),
            nn.Linear(input_size, 1000),
            nn.BatchNorm2d(1000),
            nn.ReLU(inplace=True),
            nn.Linear(1000, num_classes),
            nn.Softmax(),
        )
  
  def forward(self, h):
     d = self.layer(h)
     return d
 
      
