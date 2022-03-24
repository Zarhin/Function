import numpy as np
import matplotlib.pyplot as plt


def create_figure_by_ratio(hsize=None,
                           nrows=1,
                           ncols=1,
                           ratio=None,
                           left=0.125,
                           bottom=0.125,
                           right=0.9,
                           top=0.88,
                           wspace=0.2,
                           hspace=0.2,
                           vsize=None,
                           **kwargs):
    """Create figure and axes by given horizontal size and ratio.

    Args:
        hsize (float, optional):
            Horizontal size of figure. Defaults to None.
        nrows (int, optional):
            The number of rows of subplot grid. Defaults to 1.
        ncols (int, optional):
            The number of cols of subplot grid. Defaults to 1.
        ratio (float, optional):
            The ratio of sub_hsize to sub_vsize. Defaults to None.
        left (float, optional):
            The position of the left edge of the subplots, as a fraction of
            the figure width. Defaults to 0.125.
        bottom (float, optional):
            The position of the bottom edge of the subplots, as a fraction of
            the figure height. Defaults to 0.125.
        right (float, optional):
            The position of the right edge of the subplots, as a fraction of
            the figure width. Defaults to 0.9.
        top (float, optional):
            The position of the top edge of the subplots, as a fraction of the
            figure height. Defaults to 0.88.
        wspace (float, optional):
            The width of the padding between subplots, as a fraction of the
            average Axes width. Defaults to 0.2.
        hspace (float, optional):
            The height of the padding between subplots, as a fraction of the
            average Axes height. Defaults to 0.2.
        vsize (float, optional):
            Vertical size of figure. Defaults to None.

    Returns:
        (fig, ax): The figure and axes.
    """
    # initial
    vsize = kwargs.get('vsize', None)
    left = kwargs.get('left', 0.125)
    bottom = kwargs.get('bottom', 0.125)
    right = kwargs.get('right', 0.9)
    top = kwargs.get('top', 0.88)
    wspace = kwargs.get('wspace', 0.2)
    hspace = kwargs.get('hspace', 0.2)
    # hsize
    if not any([hsize, vsize]):
        # return default value
        return (6.4, 4.8)
    elif ratio is None:
        sub_h_fac = 1
        sub_v_fac = 1
        ratio = 4 / 3.0
    else:
        sub_h_fac = (right - left) / (ncols + (ncols - 1) * hspace)
        sub_v_fac = (top - bottom) / (nrows + (nrows - 1) * wspace)

    if hsize is not None:
        vsize = sub_h_fac * hsize / ratio / sub_v_fac
    else:
        hsize = sub_v_fac * vsize * ratio / sub_h_fac
    fig, axse = plt.subplots(nrows, ncols, figsize=(hsize, vsize), **kwargs)
    fig.subplots_adjust(left, bottom, right, top, wspace, hspace)
    return fig, axse
