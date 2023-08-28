# Assignment1

<samll> Posts Metadata </small>

| Attribute    | Description                                          |
|--------------|------------------------------------------------------|
| id           | ID of the submission.                                |
| body         | Additional description text in post body.            |
| date         | Date when the post was uploaded.                     |
| is_self      | Whether or not the submission is a selfpost (text-only). |
| flair_text   | The flair’s text content, or None if not flaired.    |
| num_comments | The number of comments on the submission.            |
| nfsw         | Whether or not the submission has been marked as NSFW (over 18). |
| score        | The number of upvotes for the submission.            |
| sticky_post  | Whether or not the submission is stickied.           |
| title        | The title of the submission.                         |
| upvote_ratio | The percentage of upvotes from all votes on the submission. |
| url          | The URL the submission links to, or the permalink if a self post. |

<samll> Comments Metadata </small>

| Attribute    | Description                                          |
|--------------|------------------------------------------------------|
| post_id      | ID of the parent post against which comment has been made. |
| comment      | The commented text.                                  |
| upvotes      | Total number of upvotes/downvotes on the comment.    |
| time         | Date time when the comment was submitted.            |
| is_submitter | Whether or not the comment has been posted by posts owner itself. |
