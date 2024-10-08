```bash
defaults read ~/Library/Group\ Containers/group.com.apple.replayd/ScreenCaptureApprovals.plist

sed -i '' 's|<date>[^<]*</date>|<date>2048-01-01T00:00:00Z</date>|g' ~/Library/Group\ Containers/group.com.apple.replayd/ScreenCaptureApprovals.plist
```