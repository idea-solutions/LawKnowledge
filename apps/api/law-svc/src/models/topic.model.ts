import {
  IsNumber,
  IsString,
  MaxLength,
  IsPositive,
  IsNotEmpty,
} from 'class-validator';
import { PartialType } from '@nestjs/mapped-types';

export class CreateTopicModel {
  @IsString({ message: 'Tên chủ đề phải là chuỗi' })
  @IsNotEmpty({ message: 'Tên chủ đề không được để trống' })
  @MaxLength(255, { message: 'Tên chủ đề không được quá 255 ký tự' })
  name: string;

  @IsNumber({}, { message: 'Thứ tự phải là số' })
  @IsPositive({ message: 'Thứ tự phải là số dương' })
  no: number;
}

export class UpdateTopicModel extends PartialType(CreateTopicModel) {}
