def make_plotly_figs():
    from plotly.tools import FigureFactory as FF

    import numpy as np

    x1 = np.random.randn(200)

    hist_data = [x1]

    group_labels = ['Group 1']

    # Create distplot with curve_type set to 'normal'
    fig = FF.create_distplot(hist_data, group_labels, bin_size=.25, show_curve=False)

    # Add title
    fig['layout'].update(title='Plot')
    return [fig]