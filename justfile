set quiet

# List available recipies
default:
  just --list --list-heading $'Available commands:\n'

# Run the main application
[no-exit-message]
run *args:
    uv --project src run src/main.py {{args}}

# Generate the stats graphs
[no-exit-message]
stats *args:
    uv --project src run src/stats_main.py {{args}}

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

# Build and open the slides
[no-exit-message]
slides:
  open slides.pdf &
  marp slides.md --pdf --output slides.pdf -w --allow-local-files
