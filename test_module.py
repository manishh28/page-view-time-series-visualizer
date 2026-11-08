import unittest

from time_series_visualizer import draw_bar_plot, draw_box_plot, draw_line_plot


class TimeSeriesVisualizerTestCase(unittest.TestCase):
    def test_line_plot(self):
        self.assertEqual(len(draw_line_plot().axes), 1)

    def test_bar_plot(self):
        self.assertEqual(len(draw_bar_plot().axes), 1)

    def test_box_plot(self):
        self.assertEqual(len(draw_box_plot().axes), 2)


if __name__ == "__main__":
    unittest.main()
