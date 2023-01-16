import matplotlib
from matplotlib import pyplot as plt
from io import BytesIO

matplotlib.use('Agg')

def graph(*args, **kwargs):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    im = ax.imshow(data)
    cbar = fig.colorbar(im, ax=ax)
    try:
        tmp = vars.getncattr('units')
        fa = tmp.replace('_', ' ')
        cbar.set_label(fa, ha='center',  wrap=True)
    except:
        pass

    var_name = i_variable.replace('_', ' ')
    ax.set_title(var_name, ha='center', y = 1.02,  wrap=True)
    ax.set_ylabel('Latitude')
    ax.set_xlabel('Longitude')
    ax.set_xticks(indexed_lons, lons, rotation=90, fontsize=8)
    ax.set_yticks(indexed_lats, lats, fontsize=8)
    fig.tight_layout()
    return fig

def get_image_data(fig):
    image_data = BytesIO()
    fig.savefig(image_data, format='png')
    plt.close(fig)
    image_data.seek(0)
    return image_data