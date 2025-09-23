set quiet

# List available recipies
default:
  just --list --list-heading $'Available commands:\n'

# Run the main application
[no-exit-message]
run *args:
    uv --project src run src/main/main.py {{args}}

# Run uv with correct project path
[no-exit-message]
uv *args:
    @uv --project src {{args}}

# Add package dependency
[no-exit-message]
add *args:
    @uv --project src add {{args}}

# Remove package dependency
[no-exit-message]
remove *args:
    @uv --project src remove {{args}}

# Build the final report
[no-exit-message]
build-doc:
  ./doc/bin/build_report.sh

# Build and open the final report
[no-exit-message]
doc:
  ./doc/bin/build_report.sh
  open ./doc/build/doc.pdf &
