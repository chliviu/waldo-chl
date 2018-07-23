import os

from subimage.subimage import SubimageChecker


class TestClass:
    nonimage_path = os.path.join('samples', 'nonimage.jpg')
    landscape_path = os.path.join('samples', 'landscape.jpg')
    portrait_path = os.path.join('samples', 'portrait.jpg')
    crop_path = os.path.join('samples', 'crop.jpg')
    original_path = os.path.join('samples', 'original.jpg')
    nonexisting_path = os.path.join('samples', 'nonexisting.jpg')

    def test_validate_fails_for_nonimage(self):
        checker = SubimageChecker(self.nonimage_path, self.landscape_path)
        assert not checker.validate_images()
        assert not checker._validate_are_images()

        checker = SubimageChecker(self.landscape_path, self.nonimage_path)
        assert not checker.validate_images()
        assert not checker._validate_are_images()

        checker = SubimageChecker(self.nonimage_path, self.nonimage_path)
        assert not checker.validate_images()
        assert not checker._validate_are_images()

    def test_validate_fails_for_nonexisting_file(self):
        checker = SubimageChecker(self.nonexisting_path, self.landscape_path)
        assert not checker.validate_images()
        assert not checker._validate_are_images()

        checker = SubimageChecker(self.landscape_path, self.nonexisting_path)
        assert not checker.validate_images()
        assert not checker._validate_are_images()

        checker = SubimageChecker(self.nonexisting_path, self.nonexisting_path)
        assert not checker.validate_images()
        assert not checker._validate_are_images()

    def test_validate_fails_for_incompatible_images(self):
        checker = SubimageChecker(self.portrait_path, self.landscape_path)
        assert not checker.validate_images()
        assert not checker._validate_image_dimensions()
        assert checker._validate_are_images()

        checker = SubimageChecker(self.landscape_path, self.portrait_path)
        assert not checker.validate_images()
        assert not checker._validate_image_dimensions()
        assert checker._validate_are_images()

    def test_validate_confirms_correct_images(self):
        checker = SubimageChecker(self.crop_path, self.original_path)
        assert checker._validate_are_images()
        assert checker._validate_image_dimensions()
        assert checker.validate_images()

        checker = SubimageChecker(self.original_path, self.crop_path)
        assert checker._validate_are_images()
        assert checker._validate_image_dimensions()
        assert checker.validate_images()

    def test_checker_doesnt_find_subimage_when_doesnt_exist(self):
        checker = SubimageChecker(self.crop_path, self.portrait_path)
        subimage = checker.check()
        assert subimage is None

    def test_checker_finds_subimage_for_crop(self):
        checker = SubimageChecker(self.crop_path, self.original_path)
        subimage = checker.check()
        assert subimage == [492, 357]

    def test_checker_finds_subimage_for_same_image(self):
        checker = SubimageChecker(self.crop_path, self.crop_path)
        subimage = checker.check()
        assert subimage == [0, 0]
