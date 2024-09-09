```bash
# remove old files
sudo rm -rf "/Users/lnp/Library/Application Support/Clash Nyanpasu"
sudo rm -rf "/Applications/Clash Nyanpasu.app/"

# install Clash Nyan and then add execution permission
sudo xattr -r -d com.apple.quarantine "/Applications/Clash Nyanpasu.app"
```