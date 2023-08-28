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

## Files and Folders
* `all_comments.csv` : contains all the scrapped comments from the 100 posts.
* `comments` : Folder with csv files for comments posts wise.
* `Labelling/100_labeled_commenst.csv` : Contains the human evaluated labels.
* `Labelling/labelled_comments.csv` : Contains the model evaluated labels
* `Labelling` : Contains the codes for model sentiment analysis.
* `Preprocessing/processed_comments.csv` : Contains the csv file for comments after preprocessing.
* `Preprocessing/Preprocessing.py` : The python file for preprocessing.
* `EDA.ipynb` : The jupyter notebook for EDA.
* `Random_Sampling_Comments.py` : The code for random sampling of the comments.
* `Krippendorff's_Alpha.py` : The code for inter annotator agreement.
* `scrape.ipynb` : The code performed by scrapping.
* `results.pdf` : The writeup for all the tasks.
* `word_cloud.pdf` : The pdf file for the word cloud of the entire corpus.