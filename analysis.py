from nibabel import nb


nii = nb.load("mri_template.nii.gz")

print(nii.header)
