set :application, "grb2"

set :deploy_to, "/var/www/html/#{application}/application"
set :deploy_via, :remote_cache

ssh_options[:forward_agent] = true

set :repository,  "git@github.com:grand-blaze-web/grb.git"
set :copy_exclude, [ '.git' ]

set :scm, :git
# Or: `accurev`, `bzr`, `cvs`, `darcs`, `git`, `mercurial`, `perforce`, `subversion` or `none`
set :branch, "main"

set :user, "foxbland"

default_run_options[:pty] = true

role :web, "*.*.*.*"                          # Your HTTP server, Apache/etc
role :app, "*.*.*.*"                          # This may be the same as your `Web` server
role :db,  "*.*.*.*", :primary => true # This is where Rails migrations will run

# if you want to clean up old releases on each deploy uncomment this:
# after "deploy:restart", "deploy:cleanup"

# if you're still using the script/reaper helper you will need
# these http://github.com/rails/irs_process_scripts

# If you are using Passenger mod_rails uncomment this:
# namespace :deploy do
#   task :start do ; end
#   task :stop do ; end
#   task :restart, :roles => :app, :except => { :no_release => true } do
#     run "#{try_sudo} touch #{File.join(current_path,'tmp','restart.txt')}"
#   end
# end


namespace :deploy do
  task :finalize_update, :except => { :no_release => true } do
    # do nothing
  end
  
  task :restart, :roles => :app, :ecept => { :no_release => true } do
    run "touch #{deploy_to}/current/scripts/*.wsgi"
  end
end