import argparse
from .get_html_from_safari import get_html

def main():
    parser = argparse.ArgumentParser(description="Get the HTML source of a URL.")
    parser.add_argument("url", nargs='?', default=None, help="The URL to get the HTML source from. (optional)")
    args = parser.parse_args()
    
    print (get_html(args.url))

if __name__ == '__main__':
    main()