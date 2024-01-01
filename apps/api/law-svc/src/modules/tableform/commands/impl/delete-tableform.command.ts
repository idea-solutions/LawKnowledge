/*
 * Copyright (c) 2023-present Hutech University. All rights reserved
 * Licensed under the MIT License
 */

import { ICommand } from '@nestjs/cqrs';

export class DeleteTableFormCommand implements ICommand {
  constructor(public readonly id: string) {}
}
