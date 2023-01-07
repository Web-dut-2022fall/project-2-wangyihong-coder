
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_listings_watch_list_commits_bid_record'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='commits',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='commit',
            new_name='comment',
        ),
    ]
