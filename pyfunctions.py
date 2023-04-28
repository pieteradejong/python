import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Pyfunctions:
	def get_env_vars(self) -> dict:
		return dict(os.environ.items())
	
	def print_env_vars(self) -> None:
		env_vars = self.get_env_vars()
		print(f"Listing environment variable names and values:")
		for k, v in env_vars.items():
			print(f"{k} \t\t\t {v}")

	def print_sys_path(self):
		env_vars = self.get_env_vars()
		path_str = env_vars.get('PATH', None)
		if path_str is None:
			print(f"{bcolors.WARNING}PATH variable not found{bcolors.ENDC}")
			return None
		
		print(*path_str.split(":"), sep="\n")

	def get_lines_for_file(self, filename):
		from subprocess import check_output
		lines, words, chars = map(int, check_output(["wc", filename]).split()[:3])
		return (lines, words, chars)


def main():
	pf = Pyfunctions()
	pf.print_sys_path()
	print(pf.get_lines_for_file(os.path.basename(__file__)))

if __name__ == "__main__":
	main()

