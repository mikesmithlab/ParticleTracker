from ParticleTrackingGui.preprocessing import preprocessing_methods as pm
from ParticleTrackingGui.general.parameters import get_method_name
import numpy as np

class Preprocessor:
    """
    Processes images using a list of methods in
    preprocessor parameters dictionary.
    """

    def __init__(self, parameters):
        self.parameters = parameters

    def process(self, frame):
        '''
        Preprocesses single frame
        '''
        for method in self.parameters['preprocess']['preprocess_method']:
            method_name, call_num = get_method_name(method)
            print(call_num)
            frame = getattr(pm, method_name)(frame, self.parameters, call_num=call_num)
        return frame

