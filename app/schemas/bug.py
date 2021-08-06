def bugEntity(bugs) -> dict:
    return {
        "id": str(bugs["_id"]),
        "platform": bugs['platform'],
        "sent_to_clickup": bugs["sent_to_clickup"],
        "sent_to_slack": bugs["sent_to_slack"],
        "title": bugs["title"],
        "description": bugs["description"],
        "reporter_email": bugs["reporter_email"],
        "category": bugs["category"],
        "app_version": bugs["app_version"],
        "bundle_id": bugs["bundle_id"],
        "branch": bugs["branch"],
        "device": bugs["device"],
        "location": bugs["location"],
        "session_duration": bugs["session_duration"],
        "screen_size": bugs["screen_size"],
        "density": bugs["density"],
        "user_data": bugs["user_data"],
        "console_log": bugs["console_log"],
        "locale": bugs["locale"],
        "media_path": bugs["media_path"],
        "clickup_task_url": bugs["clickup_task_url"],
        "created_at": bugs['created_at']
    }