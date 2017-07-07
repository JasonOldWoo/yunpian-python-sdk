'''
Created on Jun 19, 2017

@author: dzh
'''
from sdk.api.ypapi import YunpianApi, CommonResultHandler
from sdk.model.constant import YP_SMS_HOST, APIKEY, MOBILE, TEXT, VERSION_V1, \
    RESULT, VERSION_V2, SMS_STATUS, SMS_REPLY, START_TIME, END_TIME, PAGE_NUM, \
    PAGE_SIZE, SMS, TOTAL, TPL_ID, TPL_VALUE


class SmsApi(YunpianApi):
    '''
    短信接口 <a>https://www.yunpian.com/api2.0/sms.html</a>
    '''

    def init(self, clnt):
        super.init(clnt)
        self.host(clnt.conf(YP_SMS_HOST, 'https://sms.yunpian.com'))

    def send(self, param={}):
        '''
        <h1>智能匹配模板发送 only v1</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是 接收的手机号;发送多个手机号请以逗号分隔，一次不要超过1000个
        国际短信仅支持单号码发送，国际号码需包含国际地区前缀号码，格式必须是"+"号开头("+"号需要urlencode处理，否则会出现格式错误)，国际号码不以"+"开头将被认为是中国地区的号码
        （针对国际短信，mobile参数会自动格式化到E.164格式，可能会造成传入mobile参数跟后续的状态报告中的号码不一致。E.164格式说明，参见：
        https://en.wikipedia.org/wiki/E.164） 单号码：15205201314
        多号码：15205201314,15205201315 国际短信：+93701234567
        </p>
        <p>
        text String 是 短信内容 【云片网】您的验证码是1234
        </p>
        <p>
        extend String 否 扩展号。默认不开放，如有需要请联系客服申请 001
        </p>
        <p>
        uid String 否 该条短信在您业务系统内的ID，比如订单号或者短信发送记录的流水号。填写后发送状态返回值内将包含这个ID
        默认不开放，如有需要请联系客服申请 10001
        </p>
        <p>
        callback_url String 否
        本条短信状态报告推送地址。短信发送后将向这个地址推送短信发送报告。"后台-系统设置-数据推送与获取”可以做批量设置。如果后台已经设置地址的情况下，单次请求内也包含此参数，将以请求内的推送地址为准。
        </p>
        @deprecated
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE, TEXT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[RESULT]}[v])
        return self.path('send.json').post(param, h, r)



    def single_send(self, param={}):
        '''
        <h1>单条发送</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是
        接收的手机号；仅支持单号码发送；国际号码需包含国际地区前缀号码，格式必须是"+"号开头("+"号需要urlencode处理，否则会出现格式错误)，国际号码不以"+"开头将被认为是中国地区的号码
        （针对国际短信，mobile参数会自动格式化到E.164格式，可能会造成传入mobile参数跟后续的状态报告中的号码不一致。E.164格式说明，参见：
        https://en.wikipedia.org/wiki/E.164） 国内号码：15205201314
        国际号码：urlencode("+93701234567");
        </p>
        <p>
        text String 是 短信内容 【云片网】您的验证码是1234
        </p>
        <p>
        extend String 否 扩展号。默认不开放，如有需要请联系客服申请 001
        </p>
        <p>
        uid String 否 该条短信在您业务系统内的ID，比如订单号或者短信发送记录的流水号。填写后发送状态返回值内将包含这个ID
        默认不开放，如有需要请联系客服申请 10001
        </p>
        <p>
        callback_url String 否
        本条短信状态报告推送地址。短信发送后将向这个地址推送短信发送报告。"后台-系统设置-数据推送与获取”可以做批量设置。如果后台已经设置地址的情况下，单次请求内也包含此参数，将以请求内的推送地址为准。
        http://your_receive_url_address
        </p>
        Args:
            param: 
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE, TEXT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('single_send.json').post(param, h, r)


    def batch_send(self, param={}):
        '''
        <h1>批量发送</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是 接收的手机号；发送多个手机号请以逗号分隔，一次不要超过1000个。 单号码：15205201314
        多号码：15205201314,15205201315
        </p>
        <p>
        text String 是 短信内容 【云片网】您的验证码是1234
        </p>
        <p>
        extend String 否 扩展号。默认不开放，如有需要请联系客服申请 001
        </p>
        <p>
        uid String 否 该条短信在您业务系统内的ID，比如订单号或者短信发送记录的流水号。填写后发送状态返回值内将包含这个ID
        默认不开放，如有需要请联系客服申请 10001
        </p>
        <p>
        callback_url String 否
        本条短信状态报告推送地址。短信发送后将向这个地址推送短信发送报告。"后台-系统设置-数据推送与获取”可以做批量设置。如果后台已经设置地址的情况下，单次请求内也包含此参数，将以请求内的推送地址为准。
        http://your_receive_url_address
        </p>
        Args:
            param: 
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE, TEXT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('batch_send.json').post(param, h, r)


    def multi_send(self, param={}):
        '''
        <h1>个性化发送</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是
        接收的手机号；多个手机号请以逗号分隔，一次不要超过1000个且手机号个数必须与短信内容条数相等；不支持国际号码发送；
        多号码：15205201314,15205201315
        </p>
        <p>
        text String 是
        短信内容，多个短信内容请使用UTF-8做urlencode后，使用逗号分隔，一次不要超过1000条且短信内容条数必须与手机号个数相等
        内容示意：UrlEncode("【云片网】您的验证码是1234", "UTF-8") + "," +
        UrlEncode("【云片网】您的验证码是5678", "UTF-8")
        </p>
        <p>
        extend String 否 扩展号。默认不开放，如有需要请联系客服申请 001
        </p>
        <p>
        uid String 否 该条短信在您业务系统内的ID，比如订单号或者短信发送记录的流水号。填写后发送状态返回值内将包含这个ID
        默认不开放，如有需要请联系客服申请 10001
        </p>
        <p>
        callback_url String 否
        本条短信状态报告推送地址。短信发送后将向这个地址推送短信发送报告。"后台-系统设置-数据推送与获取”可以做批量设置。如果后台已经设置地址的情况下，单次请求内也包含此参数，将以请求内的推送地址为准。
        http://your_receive_url_address
        </p>
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE, TEXT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp, VERSION_V2:rsp}[v])
        return self.path('multi_send.json').post(param, h, r)


    def pull_status(self, param={}):
        '''
        <h1>获取状态报告</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        page_size Integer 否 每页个数，最大100个，默认20个 20
        </p>
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[SMS_STATUS], VERSION_V2:rsp}[v])
        return self.path('pull_status.json').post(param, h, r)


    def pull_reply(self, param={}):
        '''
        <h1>获取回复短信</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        page_size Integer 否 每页个数，最大100个，默认20个 20
        </p>
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[SMS_REPLY], VERSION_V2:rsp}[v])
        return self.path('pull_reply.json').post(param, h, r)


    def get_reply(self, param={}):
        '''
        <h1>查回复的短信</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        start_time String 是 短信回复开始时间 2013-08-11 00:00:00
        </p>
        <p>
        end_time String 是 短信回复结束时间 2013-08-12 00:00:00
        </p>
        <p>
        page_num Integer 是 页码，默认值为1 1
        </p>
        <p>
        page_size Integer 是 每页个数，最大100个 20
        </p>
        <p>
        mobile String 否 填写时只查该手机号的回复，不填时查所有的回复 15205201314
        </p>
        <p>
        return_fields 否 返回字段（暂未开放
        </p>
        <p>
        sort_fields 否 排序字段（暂未开放） 默认按提交时间降序
        </p>
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, START_TIME, END_TIME, PAGE_NUM, PAGE_SIZE])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[SMS_REPLY], VERSION_V2:rsp}[v])
        return self.path('get_reply.json').post(param, h, r)

    def get_black_word(self, param={}):
        '''
        <h1>查屏蔽词</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        text String 是 要检查的短信模板或者内容 这是一条测试短信
        </p>
        Args:
            param: 
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, TEXT])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[RESULT], VERSION_V2:rsp}[v])
        return self.path('get_black_word.json').post(param, h, r)


    def get_record(self, param={}):
        '''
        <h1>查短信发送记录</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 否 需要查询的手机号 15205201314
        </p>
        <p>
        start_time String 是 短信发送开始时间 2013-08-11 00:00:00
        </p>
        <p>
        end_time String 是 短信发送结束时间 2013-08-12 00:00:00
        </p>
        <p>
        page_num Integer 否 页码，默认值为1 1
        </p>
        <p>
        page_size Integer 否 每页个数，最大100个 20
        </p>
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, START_TIME, END_TIME])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[SMS], VERSION_V2:rsp}[v])
        return self.path('get_record.json').post(param, h, r)

    def count(self, param={}):
        '''
        <h1>统计短信条数</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        start_time String 是 短信发送开始时间 2013-08-11 00:00:00
        </p>
        <p>
        end_time String 是 短信发送结束时间 2013-08-12 00:00:00
        </p>
        <p>
        mobile String 否 需要查询的手机号 15205201314
        </p>
        <p>
        page_num Integer 否 页码，默认值为1 1
        </p>
        <p>
        page_size Integer 否 每页个数，最大100个 20
        </p>
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, START_TIME, END_TIME])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: 0 if TOTAL not in rsp else int(rsp[TOTAL]))
        return self.path('count.json').post(param, h, r)

    def tpl_send(self, param={}):
        '''
        <h1>指定模板发送 only v1</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是 接收的手机号 15205201314
        </p>
        <p>
        tpl_id Long 是 模板id 1
        </p>
        <p>
        tpl_value String 是 变量名和变量值对。请先对您的变量名和变量值分别进行urlencode再传递。使用参考：代码示例。
        注：变量名和变量值都不能为空 模板： 【#company#】您的验证码是#code#。 最终发送结果： 【云片网】您的验证码是1234。
        tplvalue=urlencode("#code#") + "=" + urlencode("1234") + "&amp;" +
        urlencode("#company#") + "=" + urlencode("云片网"); 若您直接发送报文请求则使用下面这种形式
        tplvalue=urlencode(urlencode("#code#") + "=" + urlencode("1234") + "&amp;" +
        urlencode("#company#") + "=" + urlencode("云片网"));
        </p>
        <p>
        extend String 否 扩展号。默认不开放，如有需要请联系客服申请 001
        </p>
        <p>
        uid String 否 用户自定义唯一id。最大长度不超过256的字符串。 默认不开放，如有需要请联系客服申请 10001
        </p>
        @deprecated
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE, TPL_ID, TPL_VALUE])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V1:rsp[RESULT]}[v])
        return self.path('tpl_send.json').post(param, h, r)

    def tpl_single_send(self, param={}):
        '''
        <h1>指定模板单发 only v2</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是
        接收的手机号（针对国际短信，mobile参数会自动格式化到E.164格式，可能会造成传入mobile参数跟后续的状态报告中的号码不一致。E.164格式说明，参见：
        https://en.wikipedia.org/wiki/E.164） 15205201314
        </p>
        <p>
        tpl_id Long 是 模板id 1
        </p>
        <p>
        tpl_value String 是 变量名和变量值对。请先对您的变量名和变量值分别进行urlencode再传递。使用参考：代码示例。
        注：变量名和变量值都不能为空 模板： 【#company#】您的验证码是#code#。 最终发送结果： 【云片网】您的验证码是1234。
        tplvalue=urlencode("#code#") + "=" + urlencode("1234") + "&amp;" +
        urlencode("#company#") + "=" + urlencode("云片网"); 若您直接发送报文请求则使用下面这种形式
        tplvalue=urlencode(urlencode("#code#") + "=" + urlencode("1234") + "&amp;" +
        urlencode("#company#") + "=" + urlencode("云片网"));
        </p>
        <p>
        extend String 否 扩展号。默认不开放，如有需要请联系客服申请 001
        </p>
        <p>
        uid String 否 用户自定义唯一id。最大长度不超过256的字符串。 默认不开放，如有需要请联系客服申请 10001
        </p>
        @deprecated
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE, TPL_ID, TPL_VALUE])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('tpl_single_send.json').post(param, h, r)


    def tpl_batch_send(self, param={}):
        '''
        <h1>指定模板群发 only v2</h1>
        <p>
        参数名 类型 是否必须 描述 示例
        </p>
        <p>
        apikey String 是 用户唯一标识 9b11127a9701975c734b8aee81ee3526
        </p>
        <p>
        mobile String 是
        接收的手机号（针对国际短信，mobile参数会自动格式化到E.164格式，可能会造成传入mobile参数跟后续的状态报告中的号码不一致。E.164格式说明，参见：
        https://en.wikipedia.org/wiki/E.164） 15205201314
        </p>
        <p>
        tpl_id Long 是 模板id 1
        </p>
        <p>
        tpl_value String 是 变量名和变量值对。请先对您的变量名和变量值分别进行urlencode再传递。使用参考：代码示例。
        注：变量名和变量值都不能为空 模板： 【#company#】您的验证码是#code#。 最终发送结果： 【云片网】您的验证码是1234。
        tplvalue=urlencode("#code#") + "=" + urlencode("1234") + "&amp;" +
        urlencode("#company#") + "=" + urlencode("云片网"); 若您直接发送报文请求则使用下面这种形式
        tplvalue=urlencode(urlencode("#code#") + "=" + urlencode("1234") + "&amp;" +
        urlencode("#company#") + "=" + urlencode("云片网"));
        </p>
        <p>
        extend String 否 扩展号。默认不开放，如有需要请联系客服申请 001
        </p>
        <p>
        uid String 否 用户自定义唯一id。最大长度不超过256的字符串。 默认不开放，如有需要请联系客服申请 10001
        </p>
        @deprecated
        Args:
            param:
        Results:
            Result
        '''
        r = self.verify_param(param, [APIKEY, MOBILE, TPL_ID, TPL_VALUE])
        if not r.is_succ():
            return r
        h = CommonResultHandler(self.version(), lambda v, rsp: {VERSION_V2:rsp}[v])
        return self.path('tpl_batch_send.json').post(param, h, r)

