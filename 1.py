{
 "appid": "&$.test_023..datas[8].app_id&",
 "access_token": "&$.case_100.access_token&",
 "to_users": ["&$.test_010..datas[0].uid&", "&$.test_011..datas[0].uid&", "&$.test_004..datas[0].uid&", "&$.test_005..datas[0].uid&"],
 "type": "file",
 "message": {
  "media_id":"&$.case_025.media_id&"
 },
 "msg_status": "1"
}

{
    "appid": "&$.test_022..datas[8].app_id&",
    "access_token": "&$.case_100.access_token&",
    "to_users": ["&$.test_010..datas[0].uid&", "&$.test_011..datas[0].uid&", "&$.test_004..datas[0].uid&",
                 "&$.test_005..datas[0].uid&"],
    "type":"attachment",
    "message":{
        "id":"594ccc6d20e01c077b5c9013",
        "head":{
            "text":"投票",
            "bgcolor":"FF0000",
            "tcolor":"FF0000"
        },
        "body":{
            "title":"投票",
            "content":"晚上吃什么"
        },
        "fields":[
            {
                "name":"",
                "text":"1",
                "value":"1",
                "input":{
                    "type":"radio",
                    "name":"味千拉⾯",
                    "group":"send_class"
                }
            },
            {
                "name":"",
                "text":"2",
                "value":"2",
                "input":{
                    "type":"radio",
                    "name":"海底捞",
                    "group":"send_class"
                }
            },
            {
                "name":"",
                "text":"3",
                "value":"3",
                "input":{
                    "type":"radio",
                    "name":"巴西烤肉",
                    "group":"send_class"
                }
            },
            {
                "name":"",
                "text":"4",
                "value":"4",
                "input":{
                    "type":"radio",
                    "name":"泰妃阁",
                    "group":"send_class"
                }
            },
            {
                "name":"",
                "text":"5",
                "value":"5",
                "input":{
                    "type":"radio",
                    "name":"外婆家",
                    "group":"send_class"
                }
            }
        ],
        "action":[
            {
                "text":"投票",
                "name":"send",
                "value":"vote"
            }
        ]
    }
}