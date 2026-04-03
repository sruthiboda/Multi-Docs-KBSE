css = '''
<style>
.chat-message {
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 10px;
    display: flex;
}
.chat-message.user {
    background-color: #2b313e;
    justify-content: flex-end;
}
.chat-message.bot {
    background-color: #475063;
    justify-content: flex-start;
}
.chat-message .message {
    max-width: 80%;
    padding: 10px 15px;
    border-radius: 10px;
    color: #fff;
    font-size: 14px;
}
</style>

'''

bot_template = '''
<div class="chat-message bot">
    <div class="message">🤖 {{MSG}}</div>
</div>

'''

user_template = '''
<div class="chat-message user">
    <div class="message">👤 {{MSG}}</div>
</div>
'''