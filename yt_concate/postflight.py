from step import Step

class Postflight(Step):
    def Process(self, data, inputs, utils):
        if inputs['cleanup']:
            print('in Postflight')
            channel_id = inputs['channel_id']
            serch_word = inputs['serch_word']
            if utils.output_filepath(channel_id, serch_word) and utils.video_list_file_exist(channel_id):
                utils.delete_file(channel_id)
                print('delete all the related output files')
