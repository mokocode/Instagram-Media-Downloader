#!/usr/bin/env python3

import os
import sys
import argparse
import instaloader

def download_instagram_media(username, output_dir=None, login_user=None, login_pass=None):
    """
    Download all pictures and videos from an Instagram account.
    
    Args:
        username (str): Instagram username to download media from
        output_dir (str, optional): Directory to save media. Defaults to username.
        login_user (str, optional): Instagram username for login
        login_pass (str, optional): Instagram password for login
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create an instance of Instaloader
        L = instaloader.Instaloader(
            download_pictures=True,
            download_videos=True,
            download_video_thumbnails=False,
            download_geotags=False,
            download_comments=False,
            save_metadata=False,
            compress_json=False
        )
        
        # Login if credentials provided
        if login_user and login_pass:
            try:
                print(f"Logging in as {login_user}...")
                L.login(login_user, login_pass)
                print("Login successful!")
            except instaloader.exceptions.BadCredentialsException:
                print("Error: Invalid login credentials")
                return False
            except instaloader.exceptions.TwoFactorAuthRequiredException:
                print("Error: Two-factor authentication is enabled. Please disable it temporarily or use session file.")
                return False
            except Exception as e:
                print(f"Login error: {str(e)}")
                return False
        
        # Set output directory
        if not output_dir:
            output_dir = username
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Change to the output directory
        original_dir = os.getcwd()
        os.chdir(output_dir)
        
        try:
            # Get profile
            print(f"Fetching profile for {username}...")
            profile = instaloader.Profile.from_username(L.context, username)
            
            # Download media
            print(f"Downloading media from {username}...")
            L.download_profile(profile, profile_pic_only=False)
            
            print(f"\nDownload complete! Media saved to: {os.path.abspath(output_dir)}")
            return True
            
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"Error: Profile '{username}' does not exist")
            return False
        except instaloader.exceptions.PrivateProfileNotFollowedException:
            print(f"Error: Profile '{username}' is private and you are not following it")
            return False
        except Exception as e:
            print(f"Error downloading profile: {str(e)}")
            return False
        finally:
            # Change back to original directory
            os.chdir(original_dir)
            
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Download all pictures and videos from an Instagram account')
    parser.add_argument('username', help='Instagram username to download media from')
    parser.add_argument('-o', '--output', help='Directory to save media (default: username)')
    parser.add_argument('-u', '--login-user', help='Instagram username for login')
    parser.add_argument('-p', '--login-pass', help='Instagram password for login')
    
    args = parser.parse_args()
    
    # Check if instaloader is installed
    try:
        import instaloader
    except ImportError:
        print("Error: instaloader package is not installed.")
        print("Please install it using: pip install instaloader")
        sys.exit(1)
    
    # Download media
    success = download_instagram_media(
        args.username,
        args.output,
        args.login_user,
        args.login_pass
    )
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
