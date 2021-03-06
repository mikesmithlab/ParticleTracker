experiment = {'experiment_method':('video_filename','sample', 'fps'),
              'video_filename':None,
              'bkg_img':None,#None gives default of video_filename[:-4] + '_bkgimg.png'
              'sample':'Normal Bacteria + 500nm colloids in buffer just bright',
              'fps':30,
              'metadata':None
              }

crop = {'crop_method': ('crop_box','mask_ellipse'),# 'mask_polygon',),
        'crop_box':((0, 1280), (0, 720)),#{'crop_coords': (76, 119, 944, 900),},
        'mask_ellipse': None,
        'mask_polygon': None,
        }

preprocess = {
    'preprocess_method': ('grayscale','medianblur',),#'variance'
    'grayscale':{},#'load_bkg_img':False,
    'threshold':{'threshold':[1,0,255,1],
                 'th_mode':[1,0,1,1]},
    'adaptive_threshold':{'block_size': [29,1,300,2],
                          'C': [-23, -30, 30, 1],
                          'ad_mode': [0, 0, 1, 1]
                          },
    'colour_channel':{'colour':'red'},#'green','blue'
    'distance':{},
    'blur':{'kernel':[1,1,15,2]},
    'medianblur':{'kernel':[3,1,15,2]},
    'gamma':{'gamma':[1,-1000,1000,1]},
    'subtract_bkg':{'subtract_bkg_type':'img',
                'subtract_bkg_blur_kernel': [3,1,15,2],
                'subtract_bkg_invert':[1,0,1,1],
                'subtract_bkg_norm':True
                },
    'variance':{'variance_type':'img',
                'variance_blur_kernel': [3,1,15,2],
                'variance_bkg_norm':True
                },
    'flip':{},
    }

track = {
    'track_method':('trackpy',),
    'trackpy':{'size_estimate':[7,1, 101,2],
               'invert':[0,0,1,1],
               'get_intensities':False,
               'intensity_radius':[2,1,200,1]
               },
    'hough':{'min_dist':[105,1,501,2],
              'p1':[75, 1, 201,2],
              'p2':[39, 1, 201,2],
              'min_rad':[10, 1, 301,2],
              'max_rad':[50, 1, 301,2],
             'get_intensities':True
             },
    'contours':{'noise_cutoff':[2,1,50,1],
                'area_min':[20, 1, 2000, 1],
                'area_max':[2000, 1, 20000, 1],
                'aspect':[1,1,20,1],
                'get_intensities':True
                },
    'boxes':{'noise_cutoff':[2,1,50,1],
                'area_min':[2, 1, 2000, 1],
                'area_max':[2000, 1, 20000, 1],
                'aspect':[1,1,20,1],
                'get_intensities':True
             },
    }

link = {
    'link_method':('default',),
    'default':{ 'pos_columns':None,
                'max_frame_displacement': [10,1,1000,1],
                'memory': [3,1,30,1],
                'min_frame_life': [10,1,100,1]
                #
                }
    }

postprocess = {
    'postprocess_method': ('max',),
    'smooth':{'column_name':'y',
              'output_name':'y_smooth',
              'span':[5,1,50,1],
              'method':'default'
              },
    'subtract_drift':{},
    'difference':{'column_name':'x_drift',
                  'output_name':'x_diff',
                  'span':[10,1,50,1]
                  },
    'magnitude':{'column_names':('x_diff','y_diff'),
                 'output_name':'r_diff'
    },
    'median':{'column_name':'r_diff',
                'output_name':'median_r',},

    'max':{'column_name':'r_diff',
           'output_name':'max_r',},

    'classify':{'column_name':'max_r',
                'output_name':'classifier',
                'value':[18, 1, 100, 1]
                },

    'angle':{'column_names':('x','y'),
             'output_name':'theta',
             'units':'degrees'

    },
    'rate':{'column_name':'x',
            'output_name':'vx',
            'fps':50.0,
            'method':'finite_difference'
              },
    'rate*2':{'column_name':'y',
            'output_name':'vy',
            'fps':50.0,
            'method':'finite_difference'
              },
    'neighbours':{'method':'delaunay',
                  'neighbours':6,
                  'cutoff':[50,1,200,1],
                }

    }

annotate = {
    'annotate_method': ('circles',),
    'videowriter':'opencv',#ffmpeg
    'frame_range':(0,10),#(start,stop) frame numbers
    'text_label':{'text':'BP1',
                 'position':(100,100),
                 'font_colour':(255,0,0),
                 'font_size':3,
                 'font_thickness':2
                 },
    'var_label':{'var_column':'index',
                 'position':(100,100),
                 'font_colour':(255,0,255),
                 'font_size':4,
                 'font_thickness':3
                 },
    'particle_values': {'values_column': 'particle',
                        'font_colour': (255, 0, 255),
                        'font_size': 1,
                        'font_thickness': 1
                        },
    'circles':{'radius':[6,1,1000,1],
               'cmap_type':'static',#'continuous',
               'cmap_column':'x',#For continuous
               'cmap_max':[470,1,2000,1],#For continuous
               'cmap_scale':1,
               'colour': (0,255,0),#For static
               'classifier_column': None,#For discrete or continuous
               'classifier': 1,#For discrete or continuous
               'thickness':2
               },
    'boxes':{  'cmap_type':'continuous',
               'cmap_column':'x',  #None
               'cmap_max':[1,1,2000,1],
               'cmap_scale':1,
               'thickness':2,
               'classifier_column': None,  # For discrete or continuous
               },
    'contours':{'radius':[6,1,1000,1],
               'cmap_type':'static',#'continuous',
               'cmap_column':'x',#For continuous
               'cmap_max':[470,1,2000,1],#For continuous
               'cmap_scale':1,
               'colour': (0,255,0),#For static
               'classifier_column': None,#For discrete or continuous
               'classifier': 1,#For discrete or continuous
               'thickness':2
               },
    'networks':{'classifier_column':None,
                'cmap_type':'static',#'continuous',
                'cmap_column':'x',#For continuous                      'classifier': 1,#For discrete or continuous
                'cmap_max':[470,1,2000,1],#For continuous              thickness':2
                'cmap_scale':1,
                'colour': (0,255,0),#For static
                'thickness':2
                },
    'vectors':{'dx_column':'x',
               'dy_column':'y',
               'thickness':2,
               'line_type':8,
               'tip_length':[1,1,100,1],
               'vector_scale':[1,1,2000,1],
               'cmap_type':'static',#'continuous',
               'cmap_column':'x',#For continuous
               'cmap_max':[470,1,2000,1],#For continuous
               'cmap_scale':1,
               'colour': (0,0,255),#For static
               'classifier_column':None,#For discrete or continuous
               'classifier': None,#For discrete or continuous
               'thickness':2
                },
    'trajectories':{'x_column':'x',
                'y_column':'y',
                'traj_length': [1000,0,1000,1],
                'cmap_type':'static',#'continuous',
                'cmap_column':'x',#For continuous
                'cmap_max':[470,1,2000,1],#For continuous
                'cmap_scale':1,
                'colour': (64,224,208),#For static
                'classifier_column':'classifier',#For discrete or continuous
                'classifier': 1,#For discrete or continuous
                'thickness':1
               },
    }

PARAMETERS = {
    'experiment': experiment,
    'crop': crop,
    'preprocess':preprocess,
    'track':track,
    'link':link,
    'postprocess':postprocess,
    'annotate':annotate
    }

from ParticleTrackingSimple.general.writeread_param_dict import write_paramdict_file

write_paramdict_file(PARAMETERS, '/home/mike/PycharmProjects/ParticleTrackingGui/project/param_files/trackpy.param')

