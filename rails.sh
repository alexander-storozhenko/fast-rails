# rbenv

sudo apt install rbenv
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build

apt-get install -y libreadline-dev
rbenv install RB_VERSION
eval "$(rbenv init -)"

# rails

cd ./
apt install ruby-railties
gem install bundler
bundle