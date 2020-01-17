import chats
import get_conoha
import serch_notice

#chats.post_chat("test_title", "test_contents")
#print(get_conoha.get_notice())
notice = get_conoha.get_notice()
report = serch_notice.serch_maintenance(notice)
#print(report)
for line in report:
    chats.post_chat(line['title'], line['contents'])
