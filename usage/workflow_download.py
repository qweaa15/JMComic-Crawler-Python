从……起jmcomic进口*
从……起jmcomic.cl进口JmcomicUIcl进口JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
JM_albums=""""''''
1166177


'''

# 单独下载章节
JM_photos="""



'''


定义env(定义env(名称，默认值，修剪=('[]'，'""'，"""))：env(名称，默认值，修剪=('[]'，'""'，"""))：('[]'，'""'，"""))：env(名称，默认值，修剪=('[]'，'""'，"""))：
进口操作系统
值=os.getenv(姓名，没有一个)getenv(姓名，没有一个)
如果价值是没有一个或价值=="：'':
返回默认

为一对在……内修剪：
如果价值。startswith(一对[0])和价值。endswith(一对[1])：如果价值。startswith(一对[0])和价值。endswith(一对[1])：
value=value[1：-1][1：-1]

返回价值


定义get_id_set(环境名称，给定)：get_id_set(环境名称，给定)：
aid_set=设置()设置()
为文本在……内 [[
鉴于，
(env(环境名称，")).取代('-'，'\n')，(env(环境名称，")).取代('-'，'\n')，
    ]:
(更新(str_to_set(文本)))

返回aid_set


定义 主要的():主要的():
album_id_set=get_id_set('JM_ALBUM_IDS'，jm_ablums)get_id_set('JM_ALBUM_IDS'，jm_ablums)
photo_id_set=get_id_set('JM_PHOTO_IDS'，jm_photos)get_id_set('JM_PHOTO_IDS'，jm_photos)

helper=JmcomicUI()JmcomicUI()
助手。列表(album_id_set)
助手。photo_id_list=列表(photo_id_set)

option=get_option()get_option()
助手。 跑(助手。 跑(选项))
选项。call_all_plugin('下载后')


定义get_option()：get_option()：
#读取选项配置文件#读取选项配置文件
option=create_option(操作系统。路径.abspath(操作系统。路径.参加(__file__，'.。/。。/assets/option/option_workflow_download。yml')))create_option(操作系统。路径.abspath(操作系统。路径.参加(__file__，'.。/。。/assets/option/option_workflow_download。yml')))

# 支持工作流覆盖配置文件的配置# 支持工作流覆盖配置文件的配置
cover_option_config(选项)

#把请求错误的html下载到文件，方便GitHub Actions下载查看日志#把请求错误的html下载到文件，方便GitHub操作下载查看日志
log_before_raise()log_before_raise()

返回选项


def cover_option_config(option: JmOption):
    dir_rule = env('DIR_RULE', None)
如果dir_rule不是None：
_old=option.dir_rule
_new=DirRule(dir_rule，base_dir=the_old.base_dir)
option.dir_rule=新建

impl=env('CLIENT_IMPL'，无)
如果impl不是None：
option.client.impl=impl

后缀=env('IMAGE_SUFFIX'，无)
如果后缀不是None：
option.download.image.suffix=fix_suffix(后缀)


Def log_before_raise()：
JM_download_dir=env('JM_DOWNLOAD_DIR'，workspace())
mkdir_if_not_exists(jm_download_dir)

Def decision_filepath(e)：
RESP=e.context.get(ExceptionTool.CONTEXT_KEY_RESP，None)

如果resp为None：
后缀=str(time_stamp())
        else:
            suffix = resp.url

        name = '-'.join(
            fix_windir_name(it)
            for it in [
                e.description,
                current_thread().name,
                suffix
            ]
        )

        path = f'{jm_download_dir}/【出错了】{name}.log'
        return path

    def exception_listener(e: JmcomicException):
        """
        异常监听器，实现了在 GitHub Actions 下，把请求错误的信息下载到文件，方便调试和通知使用者
        """
        # 决定要写入的文件路径
        path = decide_filepath(e)

        # 准备内容
        content = [
            str(type(e)),
            e.msg,
        ]
        for k, v in e.context.items():
            content.append(f'{k}: {v}')

        # resp.text
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)
        if resp:
            content.append(f'响应文本: {resp.text}')

        # 写文件
        write_text(path, '\n'.join(content))

    JmModuleConfig.register_exception_listener(JmcomicException, exception_listener)


if __name__ == '__main__':
    main()
