from absl import flags
from absl import app

FLAGS = flags.FLAGS

#Since Python does not have pointers, we need to define these flags as global variables
flags.DEFINE_string('name', 'Jane Random', 'Your name.')
flags.DEFINE_integer('age', None, 'Your age in years.', lower_bound=0)
flags.DEFINE_boolean('debug', False, 'Produces debugging output.')
flags.DEFINE_enum('job', 'running', ['running', 'stopped'], 'Job status.')

def main(argv):
    print('Value for name flag is {} and for integer flag is {}\n'.format(FLAGS.name, FLAGS.age))

if __name__ == "__main__":
    app.run(main)
