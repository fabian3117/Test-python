import sys

# from .consumer import Consumer
# from consumer import consumer
from consumer.consumer import Consumer

if __name__ == '__main__':
    consumer = Consumer(sys.argv[1])
    consumer.star_read()