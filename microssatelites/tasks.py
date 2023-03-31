# Celery
from celery import shared_task
# Celery-progress
from celery_progress.backend import ProgressRecorder
# Task imports
import os, time, subprocess, re
from .models import User, Project

# Celery Task
@shared_task(bind=True)
def ProcessDownload(files):
    print('Task started')
    # Create the progress recorder instance
    # which we'll use to update the web page
    progress_recorder = ProgressRecorder(self)
    print('Start')

    # CRIAR O USER NO DB COM OS DADOS DO FORMULÁRIO
    time.sleep(1)
    # progress_recorder.set_progress(description="Downloading")
    # user = User.objects.create(name=request.POST['name'], email=request.POST['email'])
    # user.save()

    # CRIAR O PROJETO NO DB
    # project = Project.objects.create(user=user)
    # project.save()
    # CRIAR PASTA DO PROJETO USER[PK]_PROJECT[PK]
    # dirproject = f'USER{user.pk}_PROJECT{project.pk}'
    # os.system(f'mkdir {dirproject}')
    # CRIAR SUBPASTAS DO PROJETO
    # subdirectories = ['UserOutputs', 'UserData', 'UserData/FASTA', 'UserData/GBKs']
    # for subdir in subdirectories:
    #     os.system(f'mkdir {dirproject}/{subdir}')
    # TRANSFERIR OS ARQUIVOS PARAS AS SUBPASTAS
    # FASTAs
    # for f in request.FILES.getlist('fileFasta'):
    #     handle_uploaded_file(f, f'{dirproject}/{subdirectories[2]}')
    # GBKs
    # for f in request.FILES.getlist('fileGBK'):
    #     handle_uploaded_file(f, f'{dirproject}/{subdirectories[3]}')
    for i in range(5):
        # Sleep for 1 second
        time.sleep(1)
        # Print progress in Celery task output
        print(i + 1)
	# 	# Update progress on the web page
        progress_recorder.set_progress(i + 1, 5, description="MudeiDownloading")
    print('End')

    return 'Task Complete'


# @shared_task(bind=True)
# def ProcessDownload(self, url):
# 	# Announce new task (celery worker output)
# 	print('Download: Task started')
#
# 	# Saved downloaded file with this name
# 	filename = 'file_download'
# 	# Wget command (5 seconds timeout)
# 	command = f'wget {url} -T 5 -O {filename}'
#
# 	# Start download process
# 	download = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# 	# Read each output line and update progress
# 	update_progress(self, download)
#
# 	# Make sure wget process is terminated
# 	download.terminate()
# 	try:
# 		# Wait 100ms
# 		download.wait(timeout=0.1)
# 		# Print return code (celery worker output)
# 		print(f'Subprocess terminated [Code {download.returncode}]')
# 	except subprocess.TimeoutExpired:
# 		# Process was not terminated in the timeout period
# 		print('Subprocess did not terminate on time')
#
# 	# Check if process was successfully completed (return code = 0)
# 	if download.returncode == 0:
# 		# Delete file
# 		try:
# 			folder = os.getcwd()
# 			filepath = os.path.join(folder, filename)
# 			os.remove(filepath)
# 		except:
# 			print('Could not delete file')
# 		# Return message to update task result
# 		return 'Download was successful!'
# 	else:
# 		# Raise exception to indicate something wrong with task
# 		raise Exception('Download timed out, try again')

def update_progress(self, proc):
	# Create progress recorder instance
	progress_recorder = ProgressRecorder(self)

	while True:
		# Read wget process output line-by-line
		line = proc.stdout.readline()

		# If line is empty: break loop (wget process completed)
		if line == b'':
			break

		linestr = line.decode('utf-8')
		if '%' in linestr:
			# Find percentage value using regex
			percentage = re.findall('[0-9]{0,3}%', linestr)[0].replace('%','')
			# Print percentage value (celery worker output)
			print(percentage)
			# Build description
			progress_description = 'Downloading (' + str(percentage) + '%)'
			# Update progress recorder
			progress_recorder.set_progress(int(percentage), 100, description=progress_description)
		else:
			# Print line
			print(linestr)

		# Sleep for 100ms
		time.sleep(0.1)
