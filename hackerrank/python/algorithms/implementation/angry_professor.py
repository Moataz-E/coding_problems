def is_canceled(test_case_class):
    """Finds whether test case class will be cancelled.

    Args:
        test_case_class: dictionary containing number of students, cancellation
            threshold, and list of student arrival times.

    Returns:
        "YES" if class is to be cancelled, and "NO" otherwise.
    """
    arrivals = 0
    threshold = test_case_class['threshold']

    for arrival_time in test_case_class['arrival_times']:
        if arrival_time > 0:
            continue
        arrivals += 1

    return "YES" if arrivals < threshold else "NO"


def prompt():
    """Prompt user for input.

    Returns:
        List of dictionaries where each dictionary represents a test case and
        contains the following keys:
            students: number of students in the class.
            threshold: cancelation threshold.
            arrival_times: list of arrival times for each student.
    """
    num_test_cases = int(input())
    test_cases_list = []

    for test_case in range(1, num_test_cases+1):
        testcase_dict = dict()

        students, threshold = input().strip().split(' ')
        testcase_dict['students'] = int(students)
        testcase_dict['threshold'] = int(threshold)

        arrival_times = [int(t) for t in input().strip().split(' ')]
        testcase_dict['arrival_times'] = arrival_times

        test_cases_list.append(testcase_dict)

    return test_cases_list

if __name__ == '__main__':
    test_cases_list = prompt()
    for test_case in test_cases_list:
        print(is_canceled(test_case))
