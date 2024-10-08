```bash
# remove old files
sudo rm -rf "/Users/lnp/Library/Application Support/Clash Nyanpasu"
sudo rm -rf "/Applications/Clash Nyanpasu.app/"

# add execute permission
sudo xattr -r -d com.apple.quarantine "/Applications/Clash Nyanpasu.app"
```