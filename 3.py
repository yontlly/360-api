{
    "appid": "&$.test_023..datas[10].app_id&",
    "access_token": "&$.case_100.access_token&",
    "to_users": ["&$.test_010..datas[0].uid&", "&$.test_011..datas[0].uid&", "&$.test_004..datas[0].uid&",
                 "&$.test_005..datas[0].uid&"],
    "type":"attachment",
    "msg_status": "1",
    "message":{
        "id":"594ccc6d20e01c077b5c9013",
        "avatartype": 1,
        "head":{
            "text":"数据选择器的测试",
            "bgcolor":"FF0000",
            "tcolor":"FF0000"
        },
        "body":{
            "title":"type类型为datapicker",
            "content":"可交互式消息",
            "image":"&$.case_022.media_id&"
        },
        "fields":[
{
                "name": "审批路径（本地数据源）",
                "input": {
                    "name": "",
                    "id": "approval",
                    "type": "datapicker",
                    "data": [
                        {
                         "text": "财务部门审批",
                            "value": "caiwu",
                            "att": {
                                "data":[
                                 {
                                 "text":"张三",
                                 "value":"zhangsan"
                                 },
                                 {
                                 "text":"李四",
                                 "value":"lisi"
                                 },
                                 {
                                 "text":"王五",
                                 "value":"wangwu"
                                 }
                                ]
                            }
                        },
                        {
                         "text": "人事部门审批",
                         "value": "renshi",
                            "att": {
                                "data":[
                                 {
                                 "text":"李雷",
                                 "value":"lilei"
                                 },
                                 {
                                 "text":"韩梅",
                                 "value":"hanmei"
                                 },
                                 {
                                 "text":"吉姆",
                                 "value":"jim"
                                 }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "name": "处理人(联动)",
                "input": {
                    "name": "",
                    "type": "datapicker",
                    "bind":{
                     "data":"approval.att.data"
                    }
                }
            },
            {
                "name": "审批路径（远程数据源）",
                "input": {
                    "name": "",
                    "id": "approvalnew",
                    "type": "datapicker",
                    "src":"http://localhost:8888/callBackDemo/src.php"
                }
            },
            {
                "name": "处理人(联动)",
                "input": {
                    "name": "",
                    "type": "datapicker",
                    "bind":{
                     "data":"approvalnew.att.data"
                    }
                }
            }
        ],
        "action": [
            {
                "name": "confirm",
                "value": "业务透传数据",
                "text": "提交",
                "color": "0F82F0",
                "confirm":{
                 "title":"确定提交吗",
                 "content":"",
                 "ok":"确定",
                 "cancel":"取消"
                }
            },
            {
                "name": "cancel",
                "value": "业务透传数据",
                "text": "取消",
                "color": "979CA4"
            }
        ]
    }
}