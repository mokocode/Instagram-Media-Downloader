# Instagram Media Downloader

This Python script downloads all pictures and videos from an Instagram account and saves them to a folder named after the account.

## Prerequisites

Before using this script, you need to install the required dependency:

```bash
pip install instaloader
```

## Usage

### Basic Usage

To download media from a public Instagram account:

```bash
python instagram_downloader.py username
```

This will create a folder with the account's username and download all media into it.

### Advanced Options

```bash
python instagram_downloader.py username -o output_directory -u your_instagram_username -p your_instagram_password
```

#### Parameters:

- `username`: The Instagram account to download media from
- `-o, --output`: Custom output directory (optional, defaults to username)
- `-u, --login-user`: Your Instagram username for authentication (required for private accounts you follow)
- `-p, --login-pass`: Your Instagram password

## Notes

- For private accounts, you must provide login credentials and be following the account
- Instagram may temporarily block access if too many requests are made in a short time
- This script respects Instagram's terms of service by using the official API through the instaloader library

## Example

```bash
# Download media from NatGeo account
python instagram_downloader.py natgeo

# Download to custom folder with authentication
python instagram_downloader.py private_friend -o friend_photos -u myusername -p mypassword
```
