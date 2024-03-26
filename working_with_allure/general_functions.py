from datetime import datetime
class GeneralFunctions:

    @staticmethod
    def read_from_logs(event, log_file, timeout=30):
        result = 0
        start_time = datetime.now()
        while result != 2:
            with open(log_file) as f:
                lines = f.readlines()
                for line, content in enumerate(lines):
                    if event in content:
                        return True, f'{event} found in log in line: {line}'
                    elif (datetime.now() - start_time).total_seconds() <= timeout:
                        continue
                    elif (datetime.now() - start_time).total_seconds() > timeout:
                        return False, f'{event} not found in log stop in line: {line}'


