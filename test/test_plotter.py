from nose.tools import assert_equals
from timegraph.drawing.plotter import Plotter

test_values = [('2015-08-18T00:00:00Z', 4.354952083333334), ('2015-08-19T00:00:00Z', 4.308158333333333),
               ('2015-08-20T00:00:00Z', 4.302979166666666), ('2015-08-21T00:00:00Z', 4.311062499999999),
               ('2015-08-22T00:00:00Z', 4.253908333333332), ('2015-08-23T00:00:00Z', 4.189418750000003),
               ('2015-08-24T00:00:00Z', 4.153933333333331), ('2015-08-25T00:00:00Z', 4.172108333333331),
               ('2015-08-26T00:00:00Z', 4.261525), ('2015-08-27T00:00:00Z', 4.292508333333336),
               ('2015-08-28T00:00:00Z', 4.4140041666666665), ('2015-08-29T00:00:00Z', 4.499274999999998),
               ('2015-08-30T00:00:00Z', 4.439795833333335), ('2015-08-31T00:00:00Z', 4.4404875000000015),
               ('2015-09-01T00:00:00Z', 4.42244375), ('2015-09-02T00:00:00Z', 4.421910416666667),
               ('2015-09-03T00:00:00Z', 4.410592436974791), ('2015-09-04T00:00:00Z', 4.3801125),
               ('2015-09-05T00:00:00Z', 4.318624217118998), ('2015-09-06T00:00:00Z', 4.288097916666669),
               ('2015-09-07T00:00:00Z', 4.393808333333334), ('2015-09-08T00:00:00Z', 4.476208333333333),
               ('2015-09-09T00:00:00Z', 4.569668750000003), ('2015-09-10T00:00:00Z', 4.60123125),
               ('2015-09-11T00:00:00Z', 4.608704166666667), ('2015-09-12T00:00:00Z', 4.658435416666667),
               ('2015-09-13T00:00:00Z', 4.7641395833333355), ('2015-09-14T00:00:00Z', 4.911522916666667),
               ('2015-09-15T00:00:00Z', 4.857977083333336), ('2015-09-16T00:00:00Z', 4.680843749999998),
               ('2015-09-17T00:00:00Z', 4.603674999999998), ('2015-09-18T00:00:00Z', 4.37027676240209)]

test_values_numbers_only = [(number) for (time, number) in test_values]

# def test_plot_timeseries():
#     plotter = Plotter()
#     plotter.plot_timeseries(test_values_numbers_only)

def test_get_y_scale():
    values = [(4.354952083333334, 7), (4.308158333333333, 7), (4.302979166666666, 7), (4.311062499999999, 7), (4.253908333333332, 7), (4.189418750000003, 7), (4.153933333333331, 7), (4.172108333333331, 7), (4.261525, 7), (4.292508333333336, 7), (4.4140041666666665, 7), (4.499274999999998, 8), (4.439795833333335, 8), (4.4404875000000015, 8), (4.42244375, 8), (4.421910416666667, 8), (4.410592436974791, 7), (4.3801125, 7), (4.318624217118998, 7), (4.288097916666669, 7), (4.393808333333334, 7), (4.476208333333333, 8), (4.569668750000003, 8), (4.60123125, 8), (4.608704166666667, 8), (4.658435416666667, 8), (4.7641395833333355, 8), (4.911522916666667, 9), (4.857977083333336, 8), (4.680843749999998, 8), (4.603674999999998, 8), (4.37027676240209, 7)]
    plotter = Plotter()
    y_scale = plotter.get_y_scale(values)
    assert_equals(max(y_scale), '4.91 ')
    assert_equals(min(y_scale), '2.64 ')
