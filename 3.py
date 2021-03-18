{
    "appid": "&$.test_023..datas[9].app_id&",
    "access_token": "&$.case_100.access_token&",
    "to_uids": ["&$.test_010..datas[0].uid&", "&$.test_011..datas[0].uid&", "&$.test_004..datas[0].uid&",
                 "&$.test_005..datas[0].uid&"],
    "type": "attachment",
    "msg_status": "1",
    "message":{
        "id":"594ccc6d20e01c077b5c9013",
        "head":{
            "text":"世界十大难题",
            "bgcolor":"FF0000",
            "tcolor":"FF0000"
        },
        "body":{
            "title":"投票",
            "content":"晚上吃什么",
            "image":"&$.case_022.media_id&"
        },
        "fields":[
            {
                "name":"晚上吃啥",
                "input":{
                    "name": "选项1",
                    "type":"radio",
                    "name":"味千拉⾯",
                    "group":"send_class",
                    "radio": true
                }
            },
            {
                "name":"",
                "input":{
                    "name": "选项2",
                    "type":"radio",
                    "name":"海底捞",
                    "group":"send_class",
                    "radio": false
                }
            },
            {
                "name":"",
                "input":{
                    "name": "选项3",
                    "type":"radio",
                    "name":"巴西烤肉",
                    "group":"send_class",
                    "radio": false
                }
            },
            {
                "name":"",
                "input":{
                    "name": "选项4",
                    "type":"radio",
                    "name":"泰妃阁",
                    "group":"send_class",
                    "radio": false
                }
            },
            {
                "name":"",
                "input":{
                    "name": "选项5",
                    "type":"radio",
                    "name":"外婆家",
                    "group":"send_class",
                    "radio": false
                }
            }
        ],
        "action": [
            {
                "name": "confirm",
                "value": "业务透传数据",
                "text": "提交",
                "color": "0F82F0",
                "confirm": {
                    "title": "确定提交吗",
                    "content": "",
                    "ok": "确定",
                    "cancel": "取消"
                }
            },
            {
                "name": "cancel",
                "value": "业务透传数据",
                "text": "取消",
                "color": "979CA4"
            }
        ]
    },
    "card":{
            "msgtotal":"1",
            "title":"股份公司总经办 王强技术管理采购流程...",
            "tcolor":"#3AA3E3",
            "url":"viewpage.action?pageId=9701578",
            "notice":"1",
            "click_to_delete":"1",
            "long_text":[
                {
                    "text":"⻓⽂本",
                    "tcolor":"#3AA3E3",
                    "fontsize":"1",
                    "rows":"1",
                    "url":"long_text&type=card"
                }
            ]
        }
}