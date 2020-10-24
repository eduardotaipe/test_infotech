from helpers import handler_response

import os
import time

class Directory():

    def data(self, path, order, sortreverse, app=None):
        directory_path = path
        data = []
        try:
            files = os.listdir(directory_path)
        except FileNotFoundError as e:
            message = f'Error: {e}'
            return handler_response(app, 400, message)
        except NotADirectoryError as e:
            message = f'Error: {e}'
            return handler_response(app, 400, message)

        for file in files:
            path_file = os.path.join(directory_path, file)
            stat = os.stat(path_file)
            file_name = file
            file_size = self.dir_size(path_file)
            create_date = self.format_date(stat.st_ctime)
            data.append({
                'file_path': directory_path,
                'filename': file_name,
                'file_create_date': create_date,
                'file_size_total': file_size[0],
                'file_size': file_size[-1],
            })

        sorted_data = sorted(data, key=lambda x: x[order], reverse=sortreverse)
        message = f'The data of the {directory_path} directory were obtained satisfactorily'

        return handler_response(app, 200, message, sorted_data)




    def dir_size(self, path): 
        raw_size = 0
        stat = os.stat(path)

        if stat.st_size > 0:
            raw_size = stat.st_size
        else:
            for dirpath, _, filenames in os.walk(path): 
                for f in filenames: 
                    full_path = os.path.join(dirpath, f) 
                    raw_size += os.path.getsize(full_path) 
        total_size = self.format_size(raw_size)
        return [total_size, raw_size]



    def format_size(self, size):
        units = ['', 'K', 'M', 'G', 'T', 'P']
        factor = 1024
        digits = 2
        suffix='B'
        
        for unit in units[:-1]:
            if size < factor:
                return f'{size:.{digits}f}{unit}{suffix}'
            size /= factor
        return f'{size:.{digits}f}{units[-1]}{suffix}'
    

    def format_date(self, full_date):
        format_type = f'%Y/%m/%d %H:%M:%S'
        format_datetime = time.strftime(format_type, time.localtime(full_date))

        return format_datetime