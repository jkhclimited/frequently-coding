import numpy
from numpy import * 

def comp_error(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2

    return totalError / float(len(points))  # Returns average

def grad_desc_runner(points, start_b, start_m, learning_rate, num_its):
    b = start_b
    m = start_m

    # Gradient descent begins here
    for i in range(num_its):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def step_gradient(b_curr, m_curr, points, step_learn_rate):
    b_grad = 0
    m_grad = 0
    n = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_grad += -(2/n) * (y - ((m_curr * x) + b_curr))
        m_grad += (2/n) * (y - ((m_curr * x) + b_curr))
    b_new = b_curr - (step_learn_rate * b_grad)
    m_new = m_curr - (step_learn_rate * m_grad)
    return [b_new, m_new]
 
def run():

    # First collect data
    points = genfromtxt('data.csv', delimiter=',')

    # Define model learning rate
    learning_rate = 0.0001
    # Eq: y = mx + b (slope formula to map out data points)
    init_b = 0
    init_m = 0
    num_its = 1000  # Number of iterations
    # Training the model time
    print('starting gradient descent at b = {0}, m = {1}, error = {2}'.format(init_b, init_m, comp_error(init_b, init_m, points)))
    [b, m] = grad_desc_runner(points, init_b, init_m, learning_rate, num_its)

    print('ending gradient descent at b = {1}, m = {2}, error = {3}'.format(num_its, b, m, comp_error(b, m, points)))

if __name__ == '__main__':
    run()