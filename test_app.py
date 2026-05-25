from app import app

def test_header_is_present(dash_duo):
    """Test to ensure the header is present."""
    dash_duo.start_server(app)
    # Wait for the H1 header to load and verify its text
    dash_duo.wait_for_element("h1", timeout=10)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualizer"

def test_visualization_is_present(dash_duo):
    """Test to ensure the visualisation (line chart) is present."""
    dash_duo.start_server(app)
    # Wait for the dcc.Graph component (which has the ID 'sales-line-chart')
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    # If the element is found within the timeout, the test passes
    assert dash_duo.find_element("#sales-line-chart")

def test_region_picker_is_present(dash_duo):
    """Test to ensure the region picker is present."""
    dash_duo.start_server(app)
    # Wait for the RadioItems component (which has the ID 'region-filter')
    dash_duo.wait_for_element("#region-filter", timeout=10)
    # If the element is found within the timeout, the test passes
    assert dash_duo.find_element("#region-filter")
