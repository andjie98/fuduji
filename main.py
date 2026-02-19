from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.all import *
from collections import defaultdict, deque

@register("fuduji", "andjie98", "复读功能插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.message_history = defaultdict(deque)  # 用于存储每个群组/频道的消息历史
        self.max_history = 10  # 最多记录最近10条消息

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    @event_message_type(EventMessageType.GROUP_MESSAGE)
    async def message_repeater(self, event: AstrMessageEvent):
        """复读功能：当超过2个玩家说相同的话时，机器人也说一句"""
        message_str = event.message_str.strip()
        
        # 忽略空消息和命令
        if not message_str or message_str.startswith('/'):
            return
        
        # 获取会话ID（群组ID或私聊ID）
        session_id = event.session_id
        user_id = event.get_sender_id()
        user_name = event.get_sender_name()
        
        # 获取消息历史
        history = self.message_history[session_id]
        
        logger.info(f"[复读插件] 收到消息: {message_str}, 发送者: {user_name}({user_id}), 当前历史数量: {len(history)}")
        
        # 统计相同消息的数量（需要来自不同用户）
        message_count = defaultdict(set)
        for msg in history:
            message_count[msg['content']].add(msg['user_id'])
        
        # 检查当前消息是否已经出现过
        if message_str in message_count:
            logger.info(f"[复读插件] 消息已出现过，说过的人数: {len(message_count[message_str])}")
            if len(message_count[message_str]) >= 2:
                logger.info(f"[复读插件] 触发复读！")
                yield event.plain_result(message_str)
            else:
                logger.info(f"[复读插件] 人数不足，不复读")
        
        # 将当前消息添加到历史记录
        history.append({
            'content': message_str,
            'user_id': user_id,
            'user_name': user_name
        })
        
        logger.info(f"[复读插件] 已添加到历史，历史数量: {len(history)}")
        
        # 保持历史记录在最大限制内
        if len(history) > self.max_history:
            history.popleft()

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        self.message_history.clear()
