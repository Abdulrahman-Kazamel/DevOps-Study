
Top 10 Processes

```bash
ps aux --sort=-%mem | head -n 11

ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -n 11
```